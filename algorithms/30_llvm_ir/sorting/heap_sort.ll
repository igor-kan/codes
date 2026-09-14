; ModuleID = 'algorithms/02_c/sorting/heap_sort.c'
source_filename = "algorithms/02_c/sorting/heap_sort.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@__const.main.data = private unnamed_addr constant [10 x i32] [i32 33, i32 7, i32 91, i32 12, i32 5, i32 5, i32 78, i32 2, i32 44, i32 19], align 16
@.str = private unnamed_addr constant [45 x i8] c"[C HeapSort] FAILED: not sorted at index %d\0A\00", align 1
@.str.1 = private unnamed_addr constant [45 x i8] c"[C HeapSort] Sift-down heap sort verified: {\00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"%d%s\00", align 1
@.str.3 = private unnamed_addr constant [3 x i8] c", \00", align 1
@.str.4 = private unnamed_addr constant [3 x i8] c"}\0A\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @heap_sort(ptr noundef captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp sgt i32 %1, 0
  br i1 %3, label %4, label %59

4:                                                ; preds = %2
  %5 = add nsw i32 %1, -2
  %6 = sdiv i32 %5, 2
  %7 = add nsw i32 %1, -1
  %8 = zext nneg i32 %6 to i64
  br label %13

9:                                                ; preds = %55
  %10 = icmp eq i32 %1, 1
  br i1 %10, label %59, label %11

11:                                               ; preds = %9
  %12 = zext nneg i32 %1 to i64
  br label %60

13:                                               ; preds = %4, %55
  %14 = phi i64 [ %8, %4 ], [ %57, %55 ]
  %15 = trunc i64 %14 to i32
  %16 = shl i32 %15, 1
  %17 = icmp slt i32 %16, %7
  br i1 %17, label %20, label %18

18:                                               ; preds = %13
  %19 = trunc nuw i64 %14 to i32
  br label %55

20:                                               ; preds = %13
  %21 = getelementptr inbounds nuw i32, ptr %0, i64 %14
  %22 = load i32, ptr %21, align 4, !tbaa !5
  %23 = trunc nuw i64 %14 to i32
  br label %24

24:                                               ; preds = %49, %20
  %25 = phi i32 [ %53, %49 ], [ %16, %20 ]
  %26 = phi i32 [ %47, %49 ], [ %23, %20 ]
  %27 = or disjoint i32 %25, 1
  %28 = zext nneg i32 %26 to i64
  %29 = getelementptr inbounds nuw i32, ptr %0, i64 %28
  %30 = zext nneg i32 %27 to i64
  %31 = getelementptr inbounds nuw i32, ptr %0, i64 %30
  %32 = load i32, ptr %31, align 4, !tbaa !5
  %33 = icmp slt i32 %22, %32
  %34 = select i1 %33, i32 %27, i32 %26
  %35 = add nuw nsw i32 %25, 2
  %36 = icmp slt i32 %35, %1
  br i1 %36, label %37, label %46

37:                                               ; preds = %24
  %38 = zext nneg i32 %34 to i64
  %39 = getelementptr inbounds nuw i32, ptr %0, i64 %38
  %40 = load i32, ptr %39, align 4, !tbaa !5
  %41 = zext nneg i32 %35 to i64
  %42 = getelementptr inbounds nuw i32, ptr %0, i64 %41
  %43 = load i32, ptr %42, align 4, !tbaa !5
  %44 = icmp slt i32 %40, %43
  %45 = select i1 %44, i32 %35, i32 %34
  br label %46

46:                                               ; preds = %37, %24
  %47 = phi i32 [ %34, %24 ], [ %45, %37 ]
  %48 = icmp eq i32 %47, %26
  br i1 %48, label %55, label %49

49:                                               ; preds = %46
  %50 = zext nneg i32 %47 to i64
  %51 = getelementptr inbounds nuw i32, ptr %0, i64 %50
  %52 = load i32, ptr %51, align 4, !tbaa !5
  store i32 %52, ptr %29, align 4, !tbaa !5
  store i32 %22, ptr %51, align 4, !tbaa !5
  %53 = shl nuw nsw i32 %47, 1
  %54 = icmp slt i32 %53, %7
  br i1 %54, label %24, label %55, !llvm.loop !9

55:                                               ; preds = %46, %49, %18
  %56 = phi i32 [ %19, %18 ], [ %23, %49 ], [ %23, %46 ]
  %57 = add nsw i64 %14, -1
  %58 = icmp sgt i32 %56, 0
  br i1 %58, label %13, label %9, !llvm.loop !11

59:                                               ; preds = %60, %101, %2, %9
  ret void

60:                                               ; preds = %11, %101
  %61 = phi i64 [ %12, %11 ], [ %62, %101 ]
  %62 = add nsw i64 %61, -1
  %63 = getelementptr inbounds nuw i32, ptr %0, i64 %62
  %64 = load i32, ptr %63, align 4, !tbaa !5
  %65 = load i32, ptr %0, align 4, !tbaa !5
  store i32 %65, ptr %63, align 4, !tbaa !5
  store i32 %64, ptr %0, align 4, !tbaa !5
  %66 = add nsw i64 %61, -2
  %67 = icmp eq i64 %66, 0
  br i1 %67, label %59, label %68

68:                                               ; preds = %60, %94
  %69 = phi i32 [ %98, %94 ], [ 0, %60 ]
  %70 = phi i32 [ %92, %94 ], [ 0, %60 ]
  %71 = or disjoint i32 %69, 1
  %72 = zext nneg i32 %70 to i64
  %73 = getelementptr inbounds nuw i32, ptr %0, i64 %72
  %74 = zext nneg i32 %71 to i64
  %75 = getelementptr inbounds nuw i32, ptr %0, i64 %74
  %76 = load i32, ptr %75, align 4, !tbaa !5
  %77 = icmp slt i32 %64, %76
  %78 = select i1 %77, i32 %71, i32 %70
  %79 = add nuw nsw i32 %69, 2
  %80 = zext nneg i32 %79 to i64
  %81 = icmp samesign ult i64 %66, %80
  br i1 %81, label %91, label %82

82:                                               ; preds = %68
  %83 = zext nneg i32 %78 to i64
  %84 = getelementptr inbounds nuw i32, ptr %0, i64 %83
  %85 = load i32, ptr %84, align 4, !tbaa !5
  %86 = zext nneg i32 %79 to i64
  %87 = getelementptr inbounds nuw i32, ptr %0, i64 %86
  %88 = load i32, ptr %87, align 4, !tbaa !5
  %89 = icmp slt i32 %85, %88
  %90 = select i1 %89, i32 %79, i32 %78
  br label %91

91:                                               ; preds = %82, %68
  %92 = phi i32 [ %78, %68 ], [ %90, %82 ]
  %93 = icmp eq i32 %92, %70
  br i1 %93, label %101, label %94

94:                                               ; preds = %91
  %95 = zext nneg i32 %92 to i64
  %96 = getelementptr inbounds nuw i32, ptr %0, i64 %95
  %97 = load i32, ptr %96, align 4, !tbaa !5
  store i32 %97, ptr %73, align 4, !tbaa !5
  store i32 %64, ptr %96, align 4, !tbaa !5
  %98 = shl nuw nsw i32 %92, 1
  %99 = zext nneg i32 %98 to i64
  %100 = icmp sgt i64 %66, %99
  br i1 %100, label %68, label %101, !llvm.loop !9

101:                                              ; preds = %91, %94
  %102 = icmp sgt i64 %61, 2
  br i1 %102, label %60, label %59, !llvm.loop !12
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [10 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #5
  call void @llvm.memcpy.p0.p0.i64(ptr noundef nonnull align 16 dereferenceable(40) %1, ptr noundef nonnull align 16 dereferenceable(40) @__const.main.data, i64 40, i1 false)
  call void @heap_sort(ptr noundef nonnull %1, i32 noundef 10)
  %2 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %3 = load i32, ptr %1, align 16, !tbaa !5
  %4 = load i32, ptr %2, align 4, !tbaa !5
  %5 = icmp sgt i32 %3, %4
  br i1 %5, label %50, label %6

6:                                                ; preds = %0
  %7 = getelementptr inbounds nuw i8, ptr %1, i64 8
  %8 = load i32, ptr %7, align 8, !tbaa !5
  %9 = icmp sgt i32 %4, %8
  br i1 %9, label %50, label %10

10:                                               ; preds = %6
  %11 = getelementptr inbounds nuw i8, ptr %1, i64 12
  %12 = load i32, ptr %11, align 4, !tbaa !5
  %13 = icmp sgt i32 %8, %12
  br i1 %13, label %50, label %14

14:                                               ; preds = %10
  %15 = getelementptr inbounds nuw i8, ptr %1, i64 16
  %16 = load i32, ptr %15, align 16, !tbaa !5
  %17 = icmp sgt i32 %12, %16
  br i1 %17, label %50, label %18

18:                                               ; preds = %14
  %19 = getelementptr inbounds nuw i8, ptr %1, i64 20
  %20 = load i32, ptr %19, align 4, !tbaa !5
  %21 = icmp sgt i32 %16, %20
  br i1 %21, label %50, label %22

22:                                               ; preds = %18
  %23 = getelementptr inbounds nuw i8, ptr %1, i64 24
  %24 = load i32, ptr %23, align 8, !tbaa !5
  %25 = icmp sgt i32 %20, %24
  br i1 %25, label %50, label %26

26:                                               ; preds = %22
  %27 = getelementptr inbounds nuw i8, ptr %1, i64 28
  %28 = load i32, ptr %27, align 4, !tbaa !5
  %29 = icmp sgt i32 %24, %28
  br i1 %29, label %50, label %30

30:                                               ; preds = %26
  %31 = getelementptr inbounds nuw i8, ptr %1, i64 32
  %32 = load i32, ptr %31, align 16, !tbaa !5
  %33 = icmp sgt i32 %28, %32
  br i1 %33, label %50, label %34

34:                                               ; preds = %30
  %35 = getelementptr inbounds nuw i8, ptr %1, i64 36
  %36 = load i32, ptr %35, align 4, !tbaa !5
  %37 = icmp sgt i32 %32, %36
  br i1 %37, label %50, label %38

38:                                               ; preds = %34
  %39 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.1)
  %40 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %3, ptr noundef nonnull @.str.3)
  %41 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %4, ptr noundef nonnull @.str.3)
  %42 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %8, ptr noundef nonnull @.str.3)
  %43 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %12, ptr noundef nonnull @.str.3)
  %44 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %16, ptr noundef nonnull @.str.3)
  %45 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %20, ptr noundef nonnull @.str.3)
  %46 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %24, ptr noundef nonnull @.str.3)
  %47 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %28, ptr noundef nonnull @.str.3)
  %48 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %32, ptr noundef nonnull @.str.3)
  %49 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.2, i32 noundef %36, ptr noundef nonnull @.str.4)
  br label %53

50:                                               ; preds = %34, %30, %26, %22, %18, %14, %10, %6, %0
  %51 = phi i32 [ 1, %0 ], [ 2, %6 ], [ 3, %10 ], [ 4, %14 ], [ 5, %18 ], [ 6, %22 ], [ 7, %26 ], [ 8, %30 ], [ 9, %34 ]
  %52 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %51)
  br label %53

53:                                               ; preds = %38, %50
  %54 = phi i32 [ 1, %50 ], [ 0, %38 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  ret i32 %54
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias writeonly captures(none), ptr noalias readonly captures(none), i64, i1 immarg) #3

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #4 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
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
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
!12 = distinct !{!12, !10}
