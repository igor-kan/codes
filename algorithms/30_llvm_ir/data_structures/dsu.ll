; ModuleID = 'algorithms/02_c/data_structures/dsu.c'
source_filename = "algorithms/02_c/data_structures/dsu.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.DSU = type { [1000 x i32], [1000 x i32] }

@str = private unnamed_addr constant [50 x i8] c"[C DSU] Union-by-size + path compression verified\00", align 1
@str.4 = private unnamed_addr constant [36 x i8] c"[C DSU] FAILED: merged connectivity\00", align 1
@str.5 = private unnamed_addr constant [35 x i8] c"[C DSU] FAILED: false connectivity\00", align 1
@str.6 = private unnamed_addr constant [40 x i8] c"[C DSU] FAILED: transitive connectivity\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: write) uwtable
define dso_local void @dsu_init(ptr noundef writeonly captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp sgt i32 %1, 0
  br i1 %3, label %4, label %22

4:                                                ; preds = %2
  %5 = getelementptr inbounds nuw i8, ptr %0, i64 4000
  %6 = zext nneg i32 %1 to i64
  %7 = icmp ult i32 %1, 4
  br i1 %7, label %20, label %8

8:                                                ; preds = %4
  %9 = and i64 %6, 2147483644
  br label %10

10:                                               ; preds = %10, %8
  %11 = phi i64 [ 0, %8 ], [ %15, %10 ]
  %12 = phi <4 x i32> [ <i32 0, i32 1, i32 2, i32 3>, %8 ], [ %16, %10 ]
  %13 = getelementptr inbounds nuw i32, ptr %0, i64 %11
  store <4 x i32> %12, ptr %13, align 4, !tbaa !5
  %14 = getelementptr inbounds nuw i32, ptr %5, i64 %11
  store <4 x i32> splat (i32 1), ptr %14, align 4, !tbaa !5
  %15 = add nuw i64 %11, 4
  %16 = add <4 x i32> %12, splat (i32 4)
  %17 = icmp eq i64 %15, %9
  br i1 %17, label %18, label %10, !llvm.loop !9

18:                                               ; preds = %10
  %19 = icmp eq i64 %9, %6
  br i1 %19, label %22, label %20

20:                                               ; preds = %4, %18
  %21 = phi i64 [ 0, %4 ], [ %9, %18 ]
  br label %23

22:                                               ; preds = %23, %18, %2
  ret void

23:                                               ; preds = %20, %23
  %24 = phi i64 [ %28, %23 ], [ %21, %20 ]
  %25 = getelementptr inbounds nuw i32, ptr %0, i64 %24
  %26 = trunc nuw nsw i64 %24 to i32
  store i32 %26, ptr %25, align 4, !tbaa !5
  %27 = getelementptr inbounds nuw i32, ptr %5, i64 %24
  store i32 1, ptr %27, align 4, !tbaa !5
  %28 = add nuw nsw i64 %24, 1
  %29 = icmp eq i64 %28, %6
  br i1 %29, label %22, label %23, !llvm.loop !13
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local i32 @dsu_find(ptr noundef captures(none) %0, i32 noundef %1) local_unnamed_addr #2 {
  %3 = sext i32 %1 to i64
  %4 = getelementptr inbounds i32, ptr %0, i64 %3
  %5 = load i32, ptr %4, align 4, !tbaa !5
  %6 = icmp eq i32 %5, %1
  br i1 %6, label %7, label %9

7:                                                ; preds = %2, %9
  %8 = phi i32 [ %10, %9 ], [ %1, %2 ]
  ret i32 %8

9:                                                ; preds = %2
  %10 = tail call i32 @dsu_find(ptr noundef nonnull %0, i32 noundef %5)
  store i32 %10, ptr %4, align 4, !tbaa !5
  br label %7
}

; Function Attrs: nofree nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @dsu_union(ptr noundef captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #2 {
  %4 = tail call i32 @dsu_find(ptr noundef %0, i32 noundef %1)
  %5 = tail call i32 @dsu_find(ptr noundef %0, i32 noundef %2)
  %6 = icmp eq i32 %4, %5
  br i1 %6, label %26, label %7

7:                                                ; preds = %3
  %8 = getelementptr inbounds nuw i8, ptr %0, i64 4000
  %9 = sext i32 %4 to i64
  %10 = getelementptr inbounds i32, ptr %8, i64 %9
  %11 = load i32, ptr %10, align 4, !tbaa !5
  %12 = sext i32 %5 to i64
  %13 = getelementptr inbounds i32, ptr %8, i64 %12
  %14 = load i32, ptr %13, align 4, !tbaa !5
  %15 = icmp slt i32 %11, %14
  %16 = select i1 %15, i32 %4, i32 %5
  %17 = select i1 %15, i32 %5, i32 %4
  %18 = sext i32 %16 to i64
  %19 = getelementptr inbounds i32, ptr %0, i64 %18
  store i32 %17, ptr %19, align 4, !tbaa !5
  %20 = getelementptr inbounds i32, ptr %8, i64 %18
  %21 = load i32, ptr %20, align 4, !tbaa !5
  %22 = sext i32 %17 to i64
  %23 = getelementptr inbounds i32, ptr %8, i64 %22
  %24 = load i32, ptr %23, align 4, !tbaa !5
  %25 = add nsw i32 %24, %21
  store i32 %25, ptr %23, align 4, !tbaa !5
  br label %26

26:                                               ; preds = %3, %7
  ret void
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #3 {
  %1 = alloca %struct.DSU, align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #5
  %2 = getelementptr inbounds nuw i8, ptr %1, i64 4000
  store <4 x i32> <i32 0, i32 1, i32 2, i32 3>, ptr %1, align 16, !tbaa !5
  store <4 x i32> splat (i32 1), ptr %2, align 16, !tbaa !5
  %3 = getelementptr inbounds nuw i8, ptr %1, i64 16
  store i32 4, ptr %3, align 16, !tbaa !5
  %4 = getelementptr inbounds nuw i8, ptr %1, i64 4016
  store i32 1, ptr %4, align 16, !tbaa !5
  %5 = getelementptr inbounds nuw i8, ptr %1, i64 20
  store i32 5, ptr %5, align 4, !tbaa !5
  %6 = getelementptr inbounds nuw i8, ptr %1, i64 4020
  store i32 1, ptr %6, align 4, !tbaa !5
  %7 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 0)
  %8 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 1)
  %9 = icmp eq i32 %7, %8
  br i1 %9, label %28, label %10

10:                                               ; preds = %0
  %11 = sext i32 %7 to i64
  %12 = getelementptr inbounds i32, ptr %2, i64 %11
  %13 = load i32, ptr %12, align 4, !tbaa !5
  %14 = sext i32 %8 to i64
  %15 = getelementptr inbounds i32, ptr %2, i64 %14
  %16 = load i32, ptr %15, align 4, !tbaa !5
  %17 = icmp slt i32 %13, %16
  %18 = select i1 %17, i32 %7, i32 %8
  %19 = select i1 %17, i32 %8, i32 %7
  %20 = sext i32 %18 to i64
  %21 = getelementptr inbounds i32, ptr %1, i64 %20
  store i32 %19, ptr %21, align 4, !tbaa !5
  %22 = getelementptr inbounds i32, ptr %2, i64 %20
  %23 = load i32, ptr %22, align 4, !tbaa !5
  %24 = sext i32 %19 to i64
  %25 = getelementptr inbounds i32, ptr %2, i64 %24
  %26 = load i32, ptr %25, align 4, !tbaa !5
  %27 = add nsw i32 %26, %23
  store i32 %27, ptr %25, align 4, !tbaa !5
  br label %28

28:                                               ; preds = %0, %10
  %29 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 1)
  %30 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 2)
  %31 = icmp eq i32 %29, %30
  br i1 %31, label %50, label %32

32:                                               ; preds = %28
  %33 = sext i32 %29 to i64
  %34 = getelementptr inbounds i32, ptr %2, i64 %33
  %35 = load i32, ptr %34, align 4, !tbaa !5
  %36 = sext i32 %30 to i64
  %37 = getelementptr inbounds i32, ptr %2, i64 %36
  %38 = load i32, ptr %37, align 4, !tbaa !5
  %39 = icmp slt i32 %35, %38
  %40 = select i1 %39, i32 %29, i32 %30
  %41 = select i1 %39, i32 %30, i32 %29
  %42 = sext i32 %40 to i64
  %43 = getelementptr inbounds i32, ptr %1, i64 %42
  store i32 %41, ptr %43, align 4, !tbaa !5
  %44 = getelementptr inbounds i32, ptr %2, i64 %42
  %45 = load i32, ptr %44, align 4, !tbaa !5
  %46 = sext i32 %41 to i64
  %47 = getelementptr inbounds i32, ptr %2, i64 %46
  %48 = load i32, ptr %47, align 4, !tbaa !5
  %49 = add nsw i32 %48, %45
  store i32 %49, ptr %47, align 4, !tbaa !5
  br label %50

50:                                               ; preds = %28, %32
  %51 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 3)
  %52 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 4)
  %53 = icmp eq i32 %51, %52
  br i1 %53, label %72, label %54

54:                                               ; preds = %50
  %55 = sext i32 %51 to i64
  %56 = getelementptr inbounds i32, ptr %2, i64 %55
  %57 = load i32, ptr %56, align 4, !tbaa !5
  %58 = sext i32 %52 to i64
  %59 = getelementptr inbounds i32, ptr %2, i64 %58
  %60 = load i32, ptr %59, align 4, !tbaa !5
  %61 = icmp slt i32 %57, %60
  %62 = select i1 %61, i32 %51, i32 %52
  %63 = select i1 %61, i32 %52, i32 %51
  %64 = sext i32 %62 to i64
  %65 = getelementptr inbounds i32, ptr %1, i64 %64
  store i32 %63, ptr %65, align 4, !tbaa !5
  %66 = getelementptr inbounds i32, ptr %2, i64 %64
  %67 = load i32, ptr %66, align 4, !tbaa !5
  %68 = sext i32 %63 to i64
  %69 = getelementptr inbounds i32, ptr %2, i64 %68
  %70 = load i32, ptr %69, align 4, !tbaa !5
  %71 = add nsw i32 %70, %67
  store i32 %71, ptr %69, align 4, !tbaa !5
  br label %72

72:                                               ; preds = %50, %54
  %73 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 0)
  %74 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 2)
  %75 = icmp eq i32 %73, %74
  br i1 %75, label %76, label %108

76:                                               ; preds = %72
  %77 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 0)
  %78 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 3)
  %79 = icmp eq i32 %77, %78
  br i1 %79, label %108, label %80

80:                                               ; preds = %76
  %81 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 2)
  %82 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 4)
  %83 = icmp eq i32 %81, %82
  br i1 %83, label %102, label %84

84:                                               ; preds = %80
  %85 = sext i32 %81 to i64
  %86 = getelementptr inbounds i32, ptr %2, i64 %85
  %87 = load i32, ptr %86, align 4, !tbaa !5
  %88 = sext i32 %82 to i64
  %89 = getelementptr inbounds i32, ptr %2, i64 %88
  %90 = load i32, ptr %89, align 4, !tbaa !5
  %91 = icmp slt i32 %87, %90
  %92 = select i1 %91, i32 %81, i32 %82
  %93 = select i1 %91, i32 %82, i32 %81
  %94 = sext i32 %92 to i64
  %95 = getelementptr inbounds i32, ptr %1, i64 %94
  store i32 %93, ptr %95, align 4, !tbaa !5
  %96 = getelementptr inbounds i32, ptr %2, i64 %94
  %97 = load i32, ptr %96, align 4, !tbaa !5
  %98 = sext i32 %93 to i64
  %99 = getelementptr inbounds i32, ptr %2, i64 %98
  %100 = load i32, ptr %99, align 4, !tbaa !5
  %101 = add nsw i32 %100, %97
  store i32 %101, ptr %99, align 4, !tbaa !5
  br label %102

102:                                              ; preds = %80, %84
  %103 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 0)
  %104 = call i32 @dsu_find(ptr noundef nonnull %1, i32 noundef 3)
  %105 = icmp ne i32 %103, %104
  %106 = select i1 %105, ptr @str.4, ptr @str
  %107 = zext i1 %105 to i32
  br label %108

108:                                              ; preds = %102, %76, %72
  %109 = phi ptr [ @str.5, %76 ], [ %106, %102 ], [ @str.6, %72 ]
  %110 = phi i32 [ 1, %76 ], [ %107, %102 ], [ 1, %72 ]
  %111 = tail call i32 @puts(ptr nonnull dereferenceable(1) %109)
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  ret i32 %110
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: write) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nounwind }
attributes #5 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10, !11, !12}
!10 = !{!"llvm.loop.mustprogress"}
!11 = !{!"llvm.loop.isvectorized", i32 1}
!12 = !{!"llvm.loop.unroll.runtime.disable"}
!13 = distinct !{!13, !10, !12, !11}
