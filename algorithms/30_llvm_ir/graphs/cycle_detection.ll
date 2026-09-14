; ModuleID = 'algorithms/02_c/graphs/cycle_detection.c'
source_filename = "algorithms/02_c/graphs/cycle_detection.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@visited = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@color = internal unnamed_addr global [100 x i32] zeroinitializer, align 16
@str = private unnamed_addr constant [66 x i8] c"[C CycleDetection] Directed + undirected cycle detection verified\00", align 1
@str.3 = private unnamed_addr constant [36 x i8] c"[C CycleDetection] FAILED: directed\00", align 1
@str.4 = private unnamed_addr constant [38 x i8] c"[C CycleDetection] FAILED: undirected\00", align 1

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local range(i32 0, 2) i32 @has_cycle_undirected(ptr noundef readonly captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp sgt i32 %1, 0
  br i1 %3, label %4, label %20

4:                                                ; preds = %2
  %5 = zext nneg i32 %1 to i64
  %6 = shl nuw nsw i64 %5, 2
  tail call void @llvm.memset.p0.i64(ptr nonnull align 16 @visited, i8 0, i64 %6, i1 false), !tbaa !5
  %7 = zext nneg i32 %1 to i64
  br label %8

8:                                                ; preds = %4, %17
  %9 = phi i64 [ 0, %4 ], [ %18, %17 ]
  %10 = getelementptr inbounds nuw i32, ptr @visited, i64 %9
  %11 = load i32, ptr %10, align 4, !tbaa !5
  %12 = icmp eq i32 %11, 0
  br i1 %12, label %13, label %17

13:                                               ; preds = %8
  %14 = trunc nuw nsw i64 %9 to i32
  %15 = tail call fastcc i32 @dfs_undirected(ptr noundef %0, i32 noundef %1, i32 noundef %14, i32 noundef -1)
  %16 = icmp eq i32 %15, 0
  br i1 %16, label %17, label %20

17:                                               ; preds = %8, %13
  %18 = add nuw nsw i64 %9, 1
  %19 = icmp eq i64 %18, %7
  br i1 %19, label %20, label %8, !llvm.loop !9

20:                                               ; preds = %13, %17, %2
  %21 = phi i32 [ 0, %2 ], [ 0, %17 ], [ 1, %13 ]
  ret i32 %21
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define internal fastcc noundef range(i32 0, 2) i32 @dfs_undirected(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2, i32 noundef %3) unnamed_addr #2 {
  %5 = sext i32 %2 to i64
  %6 = getelementptr inbounds i32, ptr @visited, i64 %5
  store i32 1, ptr %6, align 4, !tbaa !5
  %7 = icmp sgt i32 %1, 0
  br i1 %7, label %8, label %30

8:                                                ; preds = %4
  %9 = getelementptr inbounds [100 x i32], ptr %0, i64 %5
  %10 = zext i32 %3 to i64
  %11 = zext nneg i32 %1 to i64
  br label %12

12:                                               ; preds = %8, %27
  %13 = phi i64 [ 0, %8 ], [ %28, %27 ]
  %14 = getelementptr inbounds nuw i32, ptr %9, i64 %13
  %15 = load i32, ptr %14, align 4, !tbaa !5
  %16 = icmp eq i32 %15, 0
  br i1 %16, label %27, label %17

17:                                               ; preds = %12
  %18 = getelementptr inbounds nuw i32, ptr @visited, i64 %13
  %19 = load i32, ptr %18, align 4, !tbaa !5
  %20 = icmp eq i32 %19, 0
  br i1 %20, label %21, label %25

21:                                               ; preds = %17
  %22 = trunc nuw nsw i64 %13 to i32
  %23 = tail call fastcc i32 @dfs_undirected(ptr noundef nonnull %0, i32 noundef %1, i32 noundef %22, i32 noundef %2)
  %24 = icmp eq i32 %23, 0
  br i1 %24, label %27, label %30

25:                                               ; preds = %17
  %26 = icmp eq i64 %13, %10
  br i1 %26, label %27, label %30

27:                                               ; preds = %21, %25, %12
  %28 = add nuw nsw i64 %13, 1
  %29 = icmp eq i64 %28, %11
  br i1 %29, label %30, label %12, !llvm.loop !11

30:                                               ; preds = %27, %21, %25, %4
  %31 = phi i32 [ 0, %4 ], [ 1, %21 ], [ 1, %25 ], [ 0, %27 ]
  ret i32 %31
}

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local range(i32 0, 2) i32 @has_cycle_directed(ptr noundef readonly captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp sgt i32 %1, 0
  br i1 %3, label %4, label %20

4:                                                ; preds = %2
  %5 = zext nneg i32 %1 to i64
  %6 = shl nuw nsw i64 %5, 2
  tail call void @llvm.memset.p0.i64(ptr nonnull align 16 @color, i8 0, i64 %6, i1 false), !tbaa !5
  %7 = zext nneg i32 %1 to i64
  br label %8

8:                                                ; preds = %4, %17
  %9 = phi i64 [ 0, %4 ], [ %18, %17 ]
  %10 = getelementptr inbounds nuw i32, ptr @color, i64 %9
  %11 = load i32, ptr %10, align 4, !tbaa !5
  %12 = icmp eq i32 %11, 0
  br i1 %12, label %13, label %17

13:                                               ; preds = %8
  %14 = trunc nuw nsw i64 %9 to i32
  %15 = tail call fastcc i32 @dfs_directed(ptr noundef %0, i32 noundef %1, i32 noundef %14)
  %16 = icmp eq i32 %15, 0
  br i1 %16, label %17, label %20

17:                                               ; preds = %8, %13
  %18 = add nuw nsw i64 %9, 1
  %19 = icmp eq i64 %18, %7
  br i1 %19, label %20, label %8, !llvm.loop !12

20:                                               ; preds = %13, %17, %2
  %21 = phi i32 [ 0, %2 ], [ 0, %17 ], [ 1, %13 ]
  ret i32 %21
}

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define internal fastcc range(i32 0, 2) i32 @dfs_directed(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) unnamed_addr #2 {
  %4 = sext i32 %2 to i64
  %5 = getelementptr inbounds i32, ptr @color, i64 %4
  store i32 1, ptr %5, align 4, !tbaa !5
  %6 = icmp sgt i32 %1, 0
  br i1 %6, label %7, label %25

7:                                                ; preds = %3
  %8 = getelementptr inbounds [100 x i32], ptr %0, i64 %4
  %9 = zext nneg i32 %1 to i64
  br label %10

10:                                               ; preds = %7, %22
  %11 = phi i64 [ 0, %7 ], [ %23, %22 ]
  %12 = getelementptr inbounds nuw i32, ptr %8, i64 %11
  %13 = load i32, ptr %12, align 4, !tbaa !5
  %14 = icmp eq i32 %13, 0
  br i1 %14, label %22, label %15

15:                                               ; preds = %10
  %16 = getelementptr inbounds nuw i32, ptr @color, i64 %11
  %17 = load i32, ptr %16, align 4, !tbaa !5
  switch i32 %17, label %22 [
    i32 1, label %26
    i32 0, label %18
  ]

18:                                               ; preds = %15
  %19 = trunc nuw nsw i64 %11 to i32
  %20 = tail call fastcc i32 @dfs_directed(ptr noundef nonnull %0, i32 noundef %1, i32 noundef %19)
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %26

22:                                               ; preds = %15, %18, %10
  %23 = add nuw nsw i64 %11, 1
  %24 = icmp eq i64 %23, %9
  br i1 %24, label %25, label %10, !llvm.loop !13

25:                                               ; preds = %22, %3
  store i32 2, ptr %5, align 4, !tbaa !5
  br label %26

26:                                               ; preds = %18, %15, %25
  %27 = phi i32 [ 0, %25 ], [ 1, %18 ], [ %17, %15 ]
  ret i32 %27
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #3 {
  %1 = alloca [100 x [100 x i32]], align 16
  %2 = alloca [100 x [100 x i32]], align 16
  %3 = alloca [100 x [100 x i32]], align 16
  %4 = alloca [100 x [100 x i32]], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %1, i8 0, i64 40000, i1 false)
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #6
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %2, i8 0, i64 40000, i1 false)
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #6
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %3, i8 0, i64 40000, i1 false)
  call void @llvm.lifetime.start.p0(ptr nonnull %4) #6
  call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(40000) %4, i8 0, i64 40000, i1 false)
  %5 = getelementptr inbounds nuw i8, ptr %1, i64 400
  store i32 1, ptr %5, align 16, !tbaa !5
  %6 = getelementptr inbounds nuw i8, ptr %1, i64 4
  store i32 1, ptr %6, align 4, !tbaa !5
  %7 = getelementptr inbounds nuw i8, ptr %1, i64 800
  %8 = getelementptr inbounds nuw i8, ptr %1, i64 804
  store i32 1, ptr %8, align 4, !tbaa !5
  %9 = getelementptr inbounds nuw i8, ptr %1, i64 408
  store i32 1, ptr %9, align 8, !tbaa !5
  %10 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i32 1, ptr %10, align 8, !tbaa !5
  store i32 1, ptr %7, align 16, !tbaa !5
  %11 = getelementptr inbounds nuw i8, ptr %2, i64 400
  store i32 1, ptr %11, align 16, !tbaa !5
  %12 = getelementptr inbounds nuw i8, ptr %2, i64 4
  store i32 1, ptr %12, align 4, !tbaa !5
  %13 = getelementptr inbounds nuw i8, ptr %2, i64 804
  store i32 1, ptr %13, align 4, !tbaa !5
  %14 = getelementptr inbounds nuw i8, ptr %2, i64 408
  store i32 1, ptr %14, align 8, !tbaa !5
  %15 = getelementptr inbounds nuw i8, ptr %3, i64 800
  store i32 1, ptr %15, align 16, !tbaa !5
  %16 = getelementptr inbounds nuw i8, ptr %3, i64 408
  store i32 1, ptr %16, align 8, !tbaa !5
  %17 = getelementptr inbounds nuw i8, ptr %3, i64 4
  store i32 1, ptr %17, align 4, !tbaa !5
  %18 = getelementptr inbounds nuw i8, ptr %4, i64 408
  store i32 1, ptr %18, align 8, !tbaa !5
  %19 = getelementptr inbounds nuw i8, ptr %4, i64 4
  store i32 1, ptr %19, align 4, !tbaa !5
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(12) @visited, i8 0, i64 12, i1 false), !tbaa !5
  %20 = call fastcc i32 @dfs_undirected(ptr noundef nonnull readonly %1, i32 noundef 3, i32 noundef 0, i32 noundef -1)
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %34

22:                                               ; preds = %0
  %23 = load i32, ptr getelementptr inbounds nuw (i8, ptr @visited, i64 4), align 4, !tbaa !5
  %24 = icmp eq i32 %23, 0
  br i1 %24, label %25, label %28

25:                                               ; preds = %22
  %26 = call fastcc i32 @dfs_undirected(ptr noundef nonnull readonly %1, i32 noundef 3, i32 noundef 1, i32 noundef -1)
  %27 = icmp eq i32 %26, 0
  br i1 %27, label %28, label %34

28:                                               ; preds = %25, %22
  %29 = load i32, ptr getelementptr inbounds nuw (i8, ptr @visited, i64 8), align 8, !tbaa !5
  %30 = icmp eq i32 %29, 0
  br i1 %30, label %31, label %80

31:                                               ; preds = %28
  %32 = call fastcc i32 @dfs_undirected(ptr noundef nonnull readonly %1, i32 noundef 3, i32 noundef 2, i32 noundef -1)
  %33 = icmp eq i32 %32, 0
  br i1 %33, label %80, label %34

34:                                               ; preds = %0, %25, %31
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(12) @visited, i8 0, i64 12, i1 false), !tbaa !5
  %35 = call fastcc i32 @dfs_undirected(ptr noundef nonnull readonly %2, i32 noundef 3, i32 noundef 0, i32 noundef -1)
  %36 = icmp eq i32 %35, 0
  br i1 %36, label %37, label %80

37:                                               ; preds = %34
  %38 = load i32, ptr getelementptr inbounds nuw (i8, ptr @visited, i64 4), align 4, !tbaa !5
  %39 = icmp eq i32 %38, 0
  br i1 %39, label %40, label %43

40:                                               ; preds = %37
  %41 = call fastcc i32 @dfs_undirected(ptr noundef nonnull readonly %2, i32 noundef 3, i32 noundef 1, i32 noundef -1)
  %42 = icmp eq i32 %41, 0
  br i1 %42, label %43, label %80

43:                                               ; preds = %40, %37
  %44 = load i32, ptr getelementptr inbounds nuw (i8, ptr @visited, i64 8), align 8, !tbaa !5
  %45 = icmp eq i32 %44, 0
  br i1 %45, label %46, label %49

46:                                               ; preds = %43
  %47 = call fastcc i32 @dfs_undirected(ptr noundef nonnull readonly %2, i32 noundef 3, i32 noundef 2, i32 noundef -1)
  %48 = icmp eq i32 %47, 0
  br i1 %48, label %49, label %80

49:                                               ; preds = %43, %46
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(12) @color, i8 0, i64 12, i1 false), !tbaa !5
  %50 = call fastcc i32 @dfs_directed(ptr noundef nonnull readonly %3, i32 noundef 3, i32 noundef 0)
  %51 = icmp eq i32 %50, 0
  br i1 %51, label %52, label %64

52:                                               ; preds = %49
  %53 = load i32, ptr getelementptr inbounds nuw (i8, ptr @color, i64 4), align 4, !tbaa !5
  %54 = icmp eq i32 %53, 0
  br i1 %54, label %55, label %58

55:                                               ; preds = %52
  %56 = call fastcc i32 @dfs_directed(ptr noundef nonnull readonly %3, i32 noundef 3, i32 noundef 1)
  %57 = icmp eq i32 %56, 0
  br i1 %57, label %58, label %64

58:                                               ; preds = %55, %52
  %59 = load i32, ptr getelementptr inbounds nuw (i8, ptr @color, i64 8), align 8, !tbaa !5
  %60 = icmp eq i32 %59, 0
  br i1 %60, label %61, label %79

61:                                               ; preds = %58
  %62 = call fastcc i32 @dfs_directed(ptr noundef nonnull readonly %3, i32 noundef 3, i32 noundef 2)
  %63 = icmp eq i32 %62, 0
  br i1 %63, label %79, label %64

64:                                               ; preds = %49, %55, %61
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(12) @color, i8 0, i64 12, i1 false), !tbaa !5
  %65 = call fastcc i32 @dfs_directed(ptr noundef nonnull readonly %4, i32 noundef 3, i32 noundef 0)
  %66 = icmp eq i32 %65, 0
  br i1 %66, label %67, label %79

67:                                               ; preds = %64
  %68 = load i32, ptr getelementptr inbounds nuw (i8, ptr @color, i64 4), align 4, !tbaa !5
  %69 = icmp eq i32 %68, 0
  br i1 %69, label %70, label %73

70:                                               ; preds = %67
  %71 = call fastcc i32 @dfs_directed(ptr noundef nonnull readonly %4, i32 noundef 3, i32 noundef 1)
  %72 = icmp eq i32 %71, 0
  br i1 %72, label %73, label %79

73:                                               ; preds = %70, %67
  %74 = load i32, ptr getelementptr inbounds nuw (i8, ptr @color, i64 8), align 8, !tbaa !5
  %75 = icmp eq i32 %74, 0
  br i1 %75, label %76, label %80

76:                                               ; preds = %73
  %77 = call fastcc i32 @dfs_directed(ptr noundef nonnull readonly %4, i32 noundef 3, i32 noundef 2)
  %78 = icmp eq i32 %77, 0
  br i1 %78, label %80, label %79

79:                                               ; preds = %64, %70, %76, %58, %61
  br label %80

80:                                               ; preds = %73, %76, %31, %28, %46, %40, %34, %79
  %81 = phi ptr [ @str.4, %31 ], [ @str.3, %79 ], [ @str.4, %34 ], [ @str.4, %40 ], [ @str.4, %46 ], [ @str.4, %28 ], [ @str, %76 ], [ @str, %73 ]
  %82 = phi i32 [ 1, %31 ], [ 1, %79 ], [ 1, %34 ], [ 1, %40 ], [ 1, %46 ], [ 1, %28 ], [ 0, %76 ], [ 0, %73 ]
  %83 = tail call i32 @puts(ptr nonnull dereferenceable(1) %81)
  call void @llvm.lifetime.end.p0(ptr nonnull %4) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #6
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  ret i32 %82
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #4

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

attributes #0 = { nofree nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nosync nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
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
!13 = distinct !{!13, !10}
