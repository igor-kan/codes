; ModuleID = 'algorithms/02_c/graphs/eulerian_path.c'
source_filename = "algorithms/02_c/graphs/eulerian_path.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [44 x i8] c"[C EulerianPath] FAILED: circuit length %d\0A\00", align 1
@str = private unnamed_addr constant [54 x i8] c"[C EulerianPath] Hierholzer Eulerian circuit verified\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local i32 @hierholzer(ptr noundef captures(none) %0, i32 noundef %1, i32 noundef %2, ptr noundef captures(none) %3) local_unnamed_addr #0 {
  %5 = alloca [10000 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %5) #6
  store i32 %2, ptr %5, align 16, !tbaa !5
  %6 = icmp sgt i32 %1, 0
  %7 = zext nneg i32 %1 to i64
  br label %8

8:                                                ; preds = %4, %37
  %9 = phi i32 [ 0, %4 ], [ %39, %37 ]
  %10 = phi i32 [ 0, %4 ], [ %38, %37 ]
  %11 = zext nneg i32 %9 to i64
  %12 = getelementptr inbounds nuw i32, ptr %5, i64 %11
  %13 = load i32, ptr %12, align 4, !tbaa !5
  br i1 %6, label %14, label %32

14:                                               ; preds = %8
  %15 = sext i32 %13 to i64
  %16 = getelementptr inbounds [100 x i32], ptr %0, i64 %15
  br label %17

17:                                               ; preds = %14, %22
  %18 = phi i64 [ 0, %14 ], [ %23, %22 ]
  %19 = getelementptr inbounds nuw i32, ptr %16, i64 %18
  %20 = load i32, ptr %19, align 4, !tbaa !5
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %25

22:                                               ; preds = %17
  %23 = add nuw nsw i64 %18, 1
  %24 = icmp eq i64 %23, %7
  br i1 %24, label %32, label %17, !llvm.loop !9

25:                                               ; preds = %17
  %26 = trunc nuw nsw i64 %18 to i32
  %27 = and i64 %18, 4294967295
  %28 = getelementptr inbounds nuw i32, ptr %16, i64 %27
  store i32 0, ptr %28, align 4, !tbaa !5
  %29 = add nuw nsw i32 %9, 1
  %30 = zext nneg i32 %29 to i64
  %31 = getelementptr inbounds nuw i32, ptr %5, i64 %30
  store i32 %26, ptr %31, align 4, !tbaa !5
  br label %37

32:                                               ; preds = %22, %8
  %33 = add nsw i32 %9, -1
  %34 = add nsw i32 %10, 1
  %35 = sext i32 %10 to i64
  %36 = getelementptr inbounds i32, ptr %3, i64 %35
  store i32 %13, ptr %36, align 4, !tbaa !5
  br label %37

37:                                               ; preds = %32, %25
  %38 = phi i32 [ %10, %25 ], [ %34, %32 ]
  %39 = phi i32 [ %29, %25 ], [ %33, %32 ]
  %40 = icmp sgt i32 %39, -1
  br i1 %40, label %8, label %41, !llvm.loop !11

41:                                               ; preds = %37
  %42 = icmp sgt i32 %38, 1
  br i1 %42, label %43, label %56

43:                                               ; preds = %41
  %44 = zext nneg i32 %38 to i64
  %45 = add nsw i64 %44, -1
  br label %46

46:                                               ; preds = %46, %43
  %47 = phi i64 [ 0, %43 ], [ %53, %46 ]
  %48 = phi i64 [ %45, %43 ], [ %54, %46 ]
  %49 = getelementptr inbounds nuw i32, ptr %3, i64 %47
  %50 = load i32, ptr %49, align 4, !tbaa !5
  %51 = getelementptr inbounds i32, ptr %3, i64 %48
  %52 = load i32, ptr %51, align 4, !tbaa !5
  store i32 %52, ptr %49, align 4, !tbaa !5
  store i32 %50, ptr %51, align 4, !tbaa !5
  %53 = add nuw nsw i64 %47, 1
  %54 = add nsw i64 %48, -1
  %55 = icmp slt i64 %53, %54
  br i1 %55, label %46, label %56, !llvm.loop !12

56:                                               ; preds = %46, %41
  call void @llvm.lifetime.end.p0(ptr nonnull %5) #6
  ret i32 %38
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [10000 x i32], align 16
  %2 = alloca [100 x [100 x i32]], align 16
  %3 = alloca [10000 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #6
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %2, i8 0, i64 40000, i1 false)
  %4 = getelementptr inbounds nuw i8, ptr %2, i64 4
  store i32 1, ptr %4, align 4, !tbaa !5
  %5 = getelementptr inbounds nuw i8, ptr %2, i64 408
  store i32 1, ptr %5, align 8, !tbaa !5
  %6 = getelementptr inbounds nuw i8, ptr %2, i64 812
  store i32 1, ptr %6, align 4, !tbaa !5
  %7 = getelementptr inbounds nuw i8, ptr %2, i64 1200
  store i32 1, ptr %7, align 16, !tbaa !5
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #6
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  store i32 0, ptr %1, align 16, !tbaa !5
  br label %8

8:                                                ; preds = %42, %0
  %9 = phi i32 [ 0, %0 ], [ %44, %42 ]
  %10 = phi i32 [ 0, %0 ], [ %43, %42 ]
  %11 = zext nneg i32 %9 to i64
  %12 = getelementptr inbounds nuw i32, ptr %1, i64 %11
  %13 = load i32, ptr %12, align 4, !tbaa !5
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds [100 x i32], ptr %2, i64 %14
  %16 = load i32, ptr %15, align 16, !tbaa !5
  %17 = icmp eq i32 %16, 0
  br i1 %17, label %18, label %35

18:                                               ; preds = %8
  %19 = getelementptr inbounds nuw i8, ptr %15, i64 4
  %20 = load i32, ptr %19, align 4, !tbaa !5
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %35

22:                                               ; preds = %18
  %23 = getelementptr inbounds nuw i8, ptr %15, i64 8
  %24 = load i32, ptr %23, align 8, !tbaa !5
  %25 = icmp eq i32 %24, 0
  br i1 %25, label %26, label %35

26:                                               ; preds = %22
  %27 = getelementptr inbounds nuw i8, ptr %15, i64 12
  %28 = load i32, ptr %27, align 4, !tbaa !5
  %29 = icmp eq i32 %28, 0
  br i1 %29, label %30, label %35

30:                                               ; preds = %26
  %31 = add nsw i32 %9, -1
  %32 = add nsw i32 %10, 1
  %33 = sext i32 %10 to i64
  %34 = getelementptr inbounds i32, ptr %3, i64 %33
  store i32 %13, ptr %34, align 4, !tbaa !5
  br label %42

35:                                               ; preds = %26, %22, %18, %8
  %36 = phi i64 [ 0, %8 ], [ 1, %18 ], [ 2, %22 ], [ 3, %26 ]
  %37 = trunc nuw nsw i64 %36 to i32
  %38 = getelementptr inbounds nuw i32, ptr %15, i64 %36
  store i32 0, ptr %38, align 4, !tbaa !5
  %39 = add nuw nsw i32 %9, 1
  %40 = zext nneg i32 %39 to i64
  %41 = getelementptr inbounds nuw i32, ptr %1, i64 %40
  store i32 %37, ptr %41, align 4, !tbaa !5
  br label %42

42:                                               ; preds = %30, %35
  %43 = phi i32 [ %10, %35 ], [ %32, %30 ]
  %44 = phi i32 [ %39, %35 ], [ %31, %30 ]
  %45 = icmp sgt i32 %44, -1
  br i1 %45, label %8, label %46, !llvm.loop !11

46:                                               ; preds = %42
  %47 = icmp sgt i32 %43, 1
  br i1 %47, label %48, label %61

48:                                               ; preds = %46
  %49 = zext nneg i32 %43 to i64
  %50 = add nsw i64 %49, -1
  br label %51

51:                                               ; preds = %51, %48
  %52 = phi i64 [ 0, %48 ], [ %58, %51 ]
  %53 = phi i64 [ %50, %48 ], [ %59, %51 ]
  %54 = getelementptr inbounds nuw i32, ptr %3, i64 %52
  %55 = load i32, ptr %54, align 4, !tbaa !5
  %56 = getelementptr inbounds i32, ptr %3, i64 %53
  %57 = load i32, ptr %56, align 4, !tbaa !5
  store i32 %57, ptr %54, align 4, !tbaa !5
  store i32 %55, ptr %56, align 4, !tbaa !5
  %58 = add nuw nsw i64 %52, 1
  %59 = add nsw i64 %53, -1
  %60 = icmp slt i64 %58, %59
  br i1 %60, label %51, label %61, !llvm.loop !12

61:                                               ; preds = %51, %46
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  %62 = icmp eq i32 %43, 5
  %63 = load i32, ptr %3, align 16
  %64 = icmp eq i32 %63, 0
  %65 = select i1 %62, i1 %64, i1 false
  %66 = getelementptr inbounds nuw i8, ptr %3, i64 16
  %67 = load i32, ptr %66, align 16
  %68 = icmp eq i32 %67, 0
  %69 = select i1 %65, i1 %68, i1 false
  br i1 %69, label %72, label %70

70:                                               ; preds = %61
  %71 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %43)
  br label %74

72:                                               ; preds = %61
  %73 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %74

74:                                               ; preds = %72, %70
  %75 = phi i32 [ 1, %70 ], [ 0, %72 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #6
  ret i32 %75
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #3

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #4

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #4 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nofree nounwind }
attributes #6 = { nounwind }

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
